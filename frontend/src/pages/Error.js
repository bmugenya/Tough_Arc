import React from 'react'
import { useHistory } from 'react-router-dom'

const Error = () => {
    const history = useHistory()
    return (
        <div>
            <h2>Oops. Error Page</h2>
        </div>
    )
}

export default Error
