import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import EmployerDashboard from './pages/EmployerDashboard';

function App() {
  return (
    <Router>
      <Header />
      <div className="App">
        <header className="App-header">
          {/* Removed the logo, Learn React link, and the edit instruction */}
        </header>
        <Routes>
          <Route path="/employer-dashboard" element={<EmployerDashboard />} />
          {/* Add other routes here as needed */}
        </Routes>
      </div>
      <Footer />
    </Router>
  );
}

export default App;