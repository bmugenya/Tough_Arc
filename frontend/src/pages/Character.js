import React, { useState, useEffect } from 'react'
import { Container, Grid } from '@material-ui/core'
import axios from 'axios'
import { parse } from 'fast-xml-parser'
import ReactHtmlParser from 'react-html-parser'
import '../assets/css/Character.css'

const Character = () => {
  const [data, setData] = useState([])
  const [error, setError] = useState(null)
  const document = ReactHtmlParser(data.description)
  useEffect(() => {
    axios(
      'https://cors-anywhere.herokuapp.com/https://comicvine.gamespot.com/api/character/4005-1477/?api_key=b802f4442f13cf777d8ade8a079982e3f9e84fbd',

      {
        'Content-Type': 'application/xml; charset=utf-8',
        'Access-Control-Allow-Origin': '*',
      }
    )
      .then((response) => {
        let obj = parse(response.data)
        let newObj = obj.response.results
        console.log(newObj)
        setData(newObj)
      })
      .catch((error) => {
        console.error('Error fetching data: ', error)
        setError(error)
      })
  }, [])

  if (error) return 'Error!'

  return (
    <>
      <Container className={'top_60'}>
        <Grid container spacing={1}>
          <Grid item xs={12} sm={12} md={8}>
            {document}
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
