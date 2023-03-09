import { useEffect, useState } from 'react';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import { Link } from 'react-router-dom';
import { axios } from 'axios';
function BasicExample() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/api/item')
      .then(response => setData(response.data))
      .catch(error => console.error(error));
  }, []);
  return (
    <>
    <div className="container-fluid py-3">
      <div className="row">
        <h1 className='text-center'>Donor Page</h1>
        <Link to="/add-donor" className='p-2'><Button variant="dark">Add New Book</Button></Link>
        <div className="col-md-3">
        <Card style={{ width: '18rem' }}>
      <Card.Img variant="top" src="holder.js/100px180" />
      <Card.Body>
        <Card.Title>Book 1</Card.Title>
        <Card.Text>
          Some quick example text to build on the card title and make up the
          bulk of the card's content.
        </Card.Text>
        <Button variant="primary">Shop Now</Button>
      </Card.Body>
    </Card>
        </div>
       
        
        </div>
    </div>
   
  
    </>
  );
}

export default BasicExample;




