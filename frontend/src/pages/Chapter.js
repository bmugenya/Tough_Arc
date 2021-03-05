import React, { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import data from '../utils/data'
import IconButton from '@material-ui/core/IconButton'
import '../assets/css/Chapter.css'

const Chapter = () => {
  const [chapter, setChapter] = useState(data)
  const [isError, setIsError] = useState(false)
  const { p_id } = useParams()

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

              {Object.keys(chapters).map((detail) => (
                <div className='img-container'>
                  <img src={chapters[detail]} alt={title} />
                </div>
              ))}
            </article>
          )
        })}
      </section>
    </>
  )
}
export default Chapter
