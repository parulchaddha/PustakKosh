import './App.css';
import Navbar from './components/Navbar';
import { BrowserRouter,Route,Routes } from 'react-router-dom';
import Home from './components/home';
import Donor from './components/donor/donor';

function App() {
  return (
   <>
   <BrowserRouter>
   <Navbar/>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/donor" element={<Donor/>}/>
        
        </Routes>
    </BrowserRouter> 
   
   </> 
  );
}

export default App;
