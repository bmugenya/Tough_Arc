import React from 'react'
import { Link } from 'react-router-dom'
import data from '../utils/data'
import { useHistory } from 'react-router-dom'

const Latest = () => {
  const history = useHistory()
  return (
    <section className='container'>
      <ul>
        {data.map(({ id, title, name }) => (
          <Link to={`chapter/${id}`}>
            <li className='chapter-list' key={id}>
              {title}, {name}
            </li>
          </Link>
        ))}
      </ul>
    </section>
  )
}

export default Latest
