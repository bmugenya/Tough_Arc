import './App.css'

import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'

import Home from './pages/Home'
import Error from './pages/Error'
import Cover from './pages/Cover'
import Chapter from './pages/Chapter'
import Footer from './components/Footer'
import Character from './pages/Character'
import Contact from './pages/Contact'
import requests from './utils/requests'

function App() {
  return (
    <Router>
      <Home />
      <Switch>
        <Route exact path='/'>
          <Cover />
        </Route>
        <Route exact path='/character'>
          <Character fetchUrl={requests.fetchPanther} />
        </Route>
        <Route exact path='/contact'>
          <Contact />
        </Route>
        <Route path='/chapter/:id' children={<Chapter></Chapter>}></Route>
        <Route path='*'>
          <Error />
        </Route>
      </Switch>
      <Footer />
    </Router>
  )
}

export default App
