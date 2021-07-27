import { React, useState } from 'react'
import { Form } from '../components'
import { login } from '../auth'
import { useHistory } from 'react-router-dom'




const Contact = () => {
    const history = useHistory()
  const [emailAddress, setEmailAddress] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const url = 'www'

  const isInvalid = password === '' || emailAddress === ''
  const handleSignIn = (event) => {
    event.preventDefault()

    fetch(`${url}/rafiki/auth`, {
      method: 'POST',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        email: emailAddress,
        password: password,
      }),
    }).catch((error) => {
      setError(error.message)
      setEmailAddress('')
      setPassword('')
    })
  }
  return (
    <Form>
      <Form.Pane>
        <Form.Title>Tough Arch</Form.Title>
        <Form.Text>
         Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum
        </Form.Text>
      </Form.Pane>
      <Form.Pane>
        <Form.Block>
          <Form.Title>Subscribe</Form.Title>
          {error && <Form.Error>{error}</Form.Error>}
          <Form.Base onSubmit={handleSignIn} method='POST'>
            <Form.Input
              placeholder='Email address'
              value={emailAddress}
              onChange={({ target }) => setEmailAddress(target.value)}
            />
            <Form.Submit disabled={isInvalid} type='submit'>
              Submit
            </Form.Submit>
          </Form.Base>
        </Form.Block>
      </Form.Pane>

    </Form>
  )
}
export default Contact