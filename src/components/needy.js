import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import { Link } from 'react-router-dom';
import Dropdown from 'react-bootstrap/Dropdown';
import SearchBar from './search';

function BasicExample() {
  return (
    <>
      <div className="container-fluid py-3">
        <div className="row">
          <h1 className='text-center'>Needy Page</h1>

          <div style={{ display: 'flex', justifyContent: 'space-between' }}>

           <div style={{ display: 'flex', justifyContent: 'left',margin:'15px' }}><SearchBar/></div>
           <div></div>
            <Dropdown>
              <Dropdown.Toggle id="dropdown-button-dark-example1" variant="dark">
                Select Genre
              </Dropdown.Toggle>

              <Dropdown.Menu variant="dark">
                <Dropdown.Item href="#/action-1" active>
                  Fantasy & Science Fiction
                </Dropdown.Item>
                <Dropdown.Item href="#/action-2">Biography & autobiography</Dropdown.Item>
                <Dropdown.Item href="#/action-3">Young Adult</Dropdown.Item>
                <Dropdown.Item href="#/action-4">Educational</Dropdown.Item>
                <Dropdown.Item href="#/action-5">Inspirational & Religious</Dropdown.Item>
              </Dropdown.Menu>
            </Dropdown>

          </div>


          <div className="col-md-3">
            <Card style={{ width: '18rem', marginBottom:'15px'}}>
              <Card.Body>
                <Card.Title>Book 1</Card.Title>
                <Card.Text>
                  Some quick example text to build on the card title and make up the
                  bulk of the card's content.
                </Card.Text>
                <Button variant="primary" style={{marginRight: '10px'}}>Request </Button>
                <Button variant="primary">View Details</Button>
              </Card.Body>
            </Card>
          </div>
          <div className="col-md-3">
            <Card style={{ width: '18rem', marginBottom:'15px' }}>
              <Card.Body>
                <Card.Title>Book 2</Card.Title>
                <Card.Text>
                  Some quick example text to build on the card title and make up the
                  bulk of the card's content.
                </Card.Text>
                <Button variant="primary" style={{marginRight: '10px'}}>Request </Button>
                <Button variant="primary">View Details</Button>
              </Card.Body>
            </Card>
          </div>
          <div className="col-md-3">
            <Card style={{ width: '18rem', marginBottom:'15px' }}>
              <Card.Body>
                <Card.Title>Book 3</Card.Title>
                <Card.Text>
                  Some quick example text to build on the card title and make up the
                  bulk of the card's content.
                </Card.Text>
                <Button variant="primary" style={{marginRight: '10px'}}>Request </Button>
                <Button variant="primary">View Details</Button>
              </Card.Body>
            </Card>
          </div>
          <div className="col-md-3">
            <Card style={{ width: '18rem', marginBottom:'15px' }}>
              <Card.Body>
                <Card.Title>Book 4</Card.Title>
                <Card.Text>
                  Some quick example text to build on the card title and make up the
                  bulk of the card's content.
                </Card.Text>
                <Button variant="primary" style={{marginRight: '10px'}}>Request </Button>
                <Button variant="primary">View Details</Button>
              </Card.Body>
            </Card>
          </div>
          
          <div className="col-md-3">
            <Card style={{ width: '18rem', marginBottom:'15px' }}>
              <Card.Body>
                <Card.Title>Book 4</Card.Title>
                <Card.Text>
                  Some quick example text to build on the card title and make up the
                  bulk of the card's content.
                </Card.Text>
               <Button variant="primary" style={{marginRight: '10px'}}>Request </Button>
                <Button variant="primary">View Details</Button>
              </Card.Body>
            </Card>
          </div>
          
          <div className="col-md-3">
            <Card style={{ width: '18rem', marginBottom:'15px' }}>
              <Card.Body>
                <Card.Title>Book 5</Card.Title>
                <Card.Text>
                  Some quick example text to build on the card title and make up the
                  bulk of the card's content.
                </Card.Text>
               <Button variant="primary" style={{marginRight: '10px'}}>Request </Button>
                <Button variant="primary">View Details</Button>
              </Card.Body>
            </Card>
          </div>
          
          <div className="col-md-3">
            <Card style={{ width: '18rem', marginBottom:'15px' }}>
              <Card.Body>
                <Card.Title>Book 6</Card.Title>
                <Card.Text>
                  Some quick example text to build on the card title and make up the
                  bulk of the card's content.
                </Card.Text>
               <Button variant="primary" style={{marginRight: '10px'}}>Request </Button>
                <Button variant="primary">View Details</Button>
              </Card.Body>
            </Card>
          </div>
          
          <div className="col-md-3">
            <Card style={{ width: '18rem', marginBottom:'15px' }}>
              <Card.Body>
                <Card.Title>Book 7</Card.Title>
                <Card.Text>
                  Some quick example text to build on the card title and make up the
                  bulk of the card's content.
                </Card.Text>
               <Button variant="primary" style={{marginRight: '10px'}}>Request </Button>
                <Button variant="primary">View Details</Button>
              </Card.Body>
            </Card>
          </div>

        </div>
      </div>


    </>
  );
}

export default BasicExample;