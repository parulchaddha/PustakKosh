import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import { Link } from 'react-router-dom';
import Dropdown from 'react-bootstrap/Dropdown';


function BasicExample() {
  return (
    <>
      <div className="container-fluid py-3">
        <div className="row">
          <h1 className='text-center'>Donor Page</h1>
          <div style={{ display: 'flex', justifyContent: 'space-between' }}>

            <Link to="/add-donor" className='p-2'><Button variant="dark" > +Add New Book</Button></Link>

            <Dropdown>
              <Dropdown.Toggle id="dropdown-button-dark-example1" variant="dark">
                Check Status
              </Dropdown.Toggle>

              <Dropdown.Menu variant="dark">
                <Dropdown.Item href="#/action-1" active>
                  Active 
                </Dropdown.Item>
                <Dropdown.Item href="#/action-2">Sold</Dropdown.Item>
                <Dropdown.Item href="#/action-3">Pending</Dropdown.Item>
                <Dropdown.Divider />
                <Dropdown.Item href="#/action-4">Requested</Dropdown.Item>
              </Dropdown.Menu>
            </Dropdown>

          </div>



          <div className="col-md-3">
            <Card style={{ width: '18rem' }}>
              <Card.Body>
                <Card.Title>Book 1</Card.Title>
                <Card.Text>
                  Some quick example text to build on the card title and make up the
                  bulk of the card's content.
                </Card.Text>
                <Button variant="primary" >Check Requests</Button>
              </Card.Body>
            </Card>
          </div>
          <div className="col-md-3">
            <Card style={{ width: '18rem' }}>
              <Card.Body>
                <Card.Title>Book 2</Card.Title>
                <Card.Text>
                  Some quick example text to build on the card title and make up the
                  bulk of the card's content.
                </Card.Text>
                <Button variant="primary" onclick=" ">Check Requests</Button>
              </Card.Body>
            </Card>
          </div>
          <div className="col-md-3">
            <Card style={{ width: '18rem' }}>
              <Card.Body>
                <Card.Title>Book 3</Card.Title>
                <Card.Text>
                  Some quick example text to build on the card title and make up the
                  bulk of the card's content.
                </Card.Text>
                <Button variant="primary">Check Requests</Button>
              </Card.Body>
            </Card>
          </div>
          <div className="col-md-3">
            <Card style={{ width: '18rem' }}>
              <Card.Body>
                <Card.Title>Book 4</Card.Title>
                <Card.Text>
                  Some quick example text to build on the card title and make up the
                  bulk of the card's content.
                </Card.Text>
                <Button variant="primary">Check Requests</Button>
              </Card.Body>
            </Card>
          </div>

        </div>
      </div>


    </>
  );
}

export default BasicExample;
/*import Button from 'react-bootstrap/Button';
import { Link } from 'react-router-dom';
import ReactDOM from "react-dom/client";
import useFetch from "useFetch";
import DonorCard from './donorCard';
import React, { useState, useEffect } from 'react';

const Home = () => {
  const [data] = useFetch("url");

  return (
    <>

    <div className="container-fluid py-3">

      <div className="row">

        <h1 className='text-center'>Donor Page</h1>

        <Link to="/add-donor" className='p-2'><Button variant="dark">
        + Add New Book</Button></Link>

        {item.map((item)=> {

            return <DonorCard key={item.id} item = {item} />

        })}
        </div>
    </div>
    </>

  );
};

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Home />);

*/