import './App.css';
import Navbar from './components/Navbar';
import { BrowserRouter,Route,Routes } from 'react-router-dom';
import Home from './components/home';
import Donor from './components/donor/donor';
import Login from './components/login';
import SignUp from './components/signup';
import Needy from './components/needy';

function App() {
  return (
   <>
   <BrowserRouter>
   <Navbar/>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/donor" element={<Donor/>}/>
        <Route path="/needy" element={<Needy/>}/>
        <Route path="/login" element={<Login/>}/>
        <Route path="/signup" element={<SignUp/>}/>
        </Routes>
    </BrowserRouter> 
   
   </> 
  );
}

export default App;
