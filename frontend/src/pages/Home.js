import React from 'react'
import { Link } from 'react-router-dom'
import Banner from '../components/Banner'
import { useHistory } from 'react-router-dom'
const Home = () => {
  const history = useHistory()
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
                <Link to='/contact'>
                  <h1>Subscribe</h1>
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
