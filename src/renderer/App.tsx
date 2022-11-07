import { ChakraProvider } from '@chakra-ui/react'
import { MemoryRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/Home'


export default function App() {
  return (
    <ChakraProvider>
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
        </Routes>
      </Router>
    </ChakraProvider>
  );
}
