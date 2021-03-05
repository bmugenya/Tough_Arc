import React from 'react'
import data from '../utils/data'
import Latest from './Latest'
import '../assets/css/Cover.css'
const Cover = () => {
  return (
    <section className='container'>
      <div className='title-inner'>
        <div className='title-header'>
          <h1 className='title'>Tough Arc</h1>
        </div>

        <img
          width={333}
          height={499}
          src='https://res.cloudinary.com/dl2skiscx/image/upload/v1614781882/1_coicgr.jpg'
          alt='cover'
        />
        {data.map(({ id, author, released, status, description }) => (
          <article key={id}>
            <p>
              <strong>Author: </strong>
              {author}
              <br />
              <strong>Released: </strong>
              {released}
              <br />
              <strong>Status: </strong>
              {status}
              <br />
              <strong>Description: </strong>
              {description}
              <br />
            </p>
          </article>
        ))}
        <br />
        <br />
        <h2 className='widget'>All Chapters</h2>
        <Latest />
      </div>
    </section>
  )
}

export default Cover
