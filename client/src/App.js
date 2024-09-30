import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import EmployerDashboard from './pages/EmployerDashboard';
import CreateEmployer from './pages/CreateEmployer';

function App() {
  return (
    <Router>
      <Header />
      <div className="App">
        <header className="App-header">
          {/* Removed the logo, Learn React link, and the edit instruction */}
        </header>
        <Routes>
          <Route path="/proxy/3000/employer-dashboard" element={<EmployerDashboard />} />
          <Route path="/proxy/3000/add" element={<CreateEmployer/>}/>
        </Routes>
      </div>
      <Footer />
    </Router>
  );
}

export default App;