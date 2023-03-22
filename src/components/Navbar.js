//import './Navbar.css';
/*export default function NavBar() {
    return (
        <>
            <nav className="navbar navbar-expand-lg navbar-dark bg-dark" >
                <div className="container-fluid">
                    <a className="navbar-brand" href="#">PustakKosh</a>
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
                        <div className="navbar-nav">
                            <a className="/home" href="#">Home</a>
                            <a className="nav-link" href="#">Donor</a>
                            <a className="nav-link" href="#">Needy</a>
                            <a className="nav-link" href="#">Learn</a>
                            <a className="nav-link" href="#">Community</a>
                        </div>
                    </div>
                </div>
            </nav>
        </>
    );
}
*/
import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container';
import Form from 'react-bootstrap/Form';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';

function NavScrollExample() {
  return (
    <Navbar bg="dark" expand="lg" variant="dark">
      <Container fluid>
        <Navbar.Brand href="#">PustakKosh</Navbar.Brand>
        <Navbar.Toggle aria-controls="navbarScroll" />
        <Navbar.Collapse id="navbarScroll">
          <Nav
            className="me-auto my-2 my-lg-0"
            style={{ maxHeight: '100px' }}
            navbarScroll
          >
            <Nav.Link href="/">Home</Nav.Link>
            <Nav.Link href="/donor">Donor</Nav.Link>
            <Nav.Link href="#" >Needy</Nav.Link>
            <Nav.Link href="#" >Learn</Nav.Link>
            <Nav.Link href="#" >Community</Nav.Link>
          </Nav>
          <Nav>
          <Nav.Link href="/login"><Button variant="light">Login</Button></Nav.Link>
            <Nav.Link href="/signup">
            <Button variant="light">Signup</Button>
            </Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default NavScrollExample;
