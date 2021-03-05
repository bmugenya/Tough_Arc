import React from 'react'
import { Link } from 'react-router-dom'
import '../assets/css/Banner.css'

const Banner = () => {
  return (
    <section className='banner'>
      <h2>Gazeti</h2>
      <Link className='btn' to='/'>
        Read Tough Arc Online
      </Link>
    </section>
  )
}

export default Banner
