import React, { useState, useEffect } from 'react'
import { Container, Grid } from '@material-ui/core'
import axios from '../utils/axios'
import { parse } from 'fast-xml-parser'
import ReactHtmlParser from 'react-html-parser'
import '../assets/css/Character.css'

const Character = ({ fetchUrl }) => {
  const [data, setData] = useState([])

  const document = ReactHtmlParser(data.description)
  const doc = truncate(document, 150)

  useEffect(() => {
    async function fetchData() {
      const request = await axios.get()
      console.log(request)
      let obj = parse(request)
      // setData(obj.response.results)
      // return obj.response
    }
    fetchData()
  }, [fetchUrl])
  function truncate(str, n) {
    return str?.length > n ? str.substr(0, n - 1) + '...' : str
  }

  return (
    <>
      <Container className={'top_60'}>
        <Grid container spacing={1}>
          <Grid item xs={12} sm={12} md={8}>
            {doc}
          </Grid>
          <Grid item xs={12} sm={12} md={4}>
            <article className='wiki'>
              <h3>General Information</h3>
              <table className='table'>
                <tbody>
                  <tr>
                    <th>Super Name</th>
                    <td>{data.name}</td>
                  </tr>
                  <tr>
                    <th>Real Name</th>
                    <td>{data.real_name}</td>
                  </tr>
                  <tr>
                    <th>Alias</th>
                    <td>{data.aliases}</td>
                  </tr>
                </tbody>
              </table>
            </article>
          </Grid>
        </Grid>
      </Container>
    </>
  )
}

export default Character
