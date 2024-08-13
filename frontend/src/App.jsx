import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [message, setMessage] = useState('')

  useEffect(() => {
    const apiUrl = 'http://127.0.0.1:5000';
    console.log('VITE_API_URL:', apiUrl);
    axios.get(apiUrl)
      .then(response => setMessage(response.data.message))
      .catch(error => console.error('Error:', error))
  }, [])

  return (
    <div className="App">
      <h1>{message}</h1>
    </div>
  )
}

export default App