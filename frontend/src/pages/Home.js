import React from 'react'
import { Link } from 'react-router-dom'
import Banner from '../components/Banner'
const Home = () => {
  return (
    <>
      <Banner />
      <section className='featured'>
        <header className='featured-head'>
          <nav>
            <ul>
              <li>
                <Link to='/'>
                  <h1>Tough Arch</h1>
                </Link>
              </li>
              <li>
                <Link to='/character'>
                  <h1>Black Panther</h1>
                </Link>
              </li>
              <li>
                <Link to='/contact'>
                  <h1>Contact Us</h1>
                </Link>
              </li>
            </ul>
          </nav>
        </header>
      </section>
    </>
  )
}

export default Home
