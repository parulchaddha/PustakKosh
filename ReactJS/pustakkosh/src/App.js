import './App.css';
import Navbar from './components/Navbar';
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import Donor from './components/donor/Donor';
import Home from './components/home';

function App() {
  return (
   <>
    <BrowserRouter>
    <Navbar/>
      <Routes>
        <Route path="/" element={<Home />}></Route>
        <Route path="/donor" element={<Donor />}></Route>
      </Routes>
    </BrowserRouter> 
   </> 
  );
}


export default App;