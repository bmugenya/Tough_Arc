import React from 'react'
import { Link } from 'react-router-dom'
import '../assets/css/Footer.css'
const Footer = () => {
  return (
    <section className='footer'>
      <nav>
        <ul>
          <li>
            <Link to='/'>Tough Arc</Link>
          </li>
          <li>
            <Link to='/panther'>Black Panther</Link>
          </li>
          <li>
            <Link to='/contact'>Contact Us</Link>
          </li>
          <li>
            <Link to='/books'>Hire Me</Link>
          </li>
        </ul>
      </nav>
      <br />
      <div className='copy'>
        <p>© 2021 Tough Arc. All rights reserved</p>
      </div>
    </section>
  )
}

export default Footer
