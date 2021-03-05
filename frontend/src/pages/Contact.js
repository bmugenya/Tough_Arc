import React from 'react'
import { Grid, Typography, TextField } from '@material-ui/core'
import data from '../utils/info'
import '../assets/css/Contact.css'
import CustomButton from '../components/Button'

const Contact = () => {
  return (
    <>
      {/* Contact */}
      <Grid container spacing={6} className='section pt_45 pb_45'>
        {/* Contact form */}
        <Grid item xs={12} lg={7}>
          <Grid container>
            <Grid item className='section_title mb_30'>
              <span> </span>
              <h6 className='section_title'>Contact Form</h6>
            </Grid>
            <Grid item xs={12}>
              <Grid container spacing={3}>
                <Grid item xs={12} sm={6}>
                  <TextField fullWidth name='name' label='Name' />
                </Grid>
                <Grid item xs={12} sm={6}>
                  <TextField fullWidth name='email' label='Email' />
                </Grid>
                <Grid item xs={12}>
                  <TextField
                    fullWidth
                    name='message'
                    label='Message'
                    multiline
                    rows={4}
                  />
                </Grid>

                <Grid item xs={12}>
                  <CustomButton text='Submit' />
                </Grid>
              </Grid>
            </Grid>
          </Grid>
        </Grid>
        {/* Contact info */}
        <Grid item xs={12} lg={5}>
          <Grid container>
            <Grid item className='section_title mb_30'>
              <span> </span>
              <h6 className='section_title'>Contact Information</h6>
            </Grid>

            <Grid item xs={12}>
              <Grid container>
                <Grid item xs={12}>
                  <Typography className='contact_info'>
                    <span>Address:</span>
                    {data.address}
                  </Typography>
                </Grid>
                <Grid item xs={12}>
                  <Typography className='contact_info'>
                    <span>Phone:</span>
                    {data.phone}
                  </Typography>
                </Grid>
                <Grid item xs={12}>
                  <Typography className='contact_info'>
                    <span>Email:</span>
                    {data.email}
                  </Typography>
                </Grid>
              </Grid>
            </Grid>

            <Grid item xs={12}>
              <Grid container className='contact_box'>
                {Object.keys(data.socials).map((key) => (
                  <Grid container className='contact_social'>
                    <a href={data.socials[key].link}>
                      {data.socials[key].icon}
                    </a>
                  </Grid>
                ))}
              </Grid>
            </Grid>
          </Grid>
        </Grid>
      </Grid>
    </>
  )
}

export default Contact
