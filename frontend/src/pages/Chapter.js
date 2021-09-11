import React, { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import data from '../utils/data'
import images from '../utils/chapter.json'
import Pagination from '../components/pagination';
import IconButton from '@material-ui/core/IconButton'
import '../assets/css/Chapter.css'
import { useHistory } from 'react-router-dom'
import { useMemo } from 'react';


let PageSize = 1;
const Chapter = () => {
  const history = useHistory()
  console.log(data[0].chapters)
  const [chapter, setChapter] = useState(data)
  const [isError, setIsError] = useState(false)
    const [currentPage, setCurrentPage] = useState(1);

  const { p_id } = useParams()
  const currentTableData = useMemo(() => {


    const firstPageIndex = (currentPage - 1) * PageSize;
    const lastPageIndex = firstPageIndex + PageSize;
    return images.slice(firstPageIndex, lastPageIndex);
  }, [currentPage]);


  useEffect(() => {
    const getChapter = () => {
      setIsError(false)
      try {
        const newItems = data.filter((item) => item.id === 1)
        setChapter(newItems)
      } catch (error) {
        setIsError(true)
      }
    }
    getChapter()
  }, [])

  return (
    <>

      <section className='container'>
        {isError && <div>Something went wrong ...</div>}
        {chapter.map((item) => {
          const { id, title, cover, chapters, social } = item
          return (
            <article key={id} className='content'>
              {Object.keys(social).map((key) => (
                <IconButton href={social[key].link}>
                  {social[key].icon}
                </IconButton>
              ))}

              {currentTableData.map((chapter) => (
                <div className='img-container'>
                  <img src={chapter.content} alt={title} />
                </div>
              ))}
            </article>
          )
        })}
          <Pagination
        className="pagination-bar"
        currentPage={currentPage}
        totalCount={images.length}
        pageSize={PageSize}
        onPageChange={page => setCurrentPage(page)}
      />
      </section>
    </>
  )
}
export default Chapter
