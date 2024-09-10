import React from 'react';
import JobPostingForm from './JobPostingForm';
import JobListingManager from './JobListingManager';

const EmployerDashboard = () => {
  return (
    <div className="flex flex-col h-screen bg-white">
      {/* Header */}
      <header className="bg-blue-900 text-white fixed w-full z-10">
        <div className="flex justify-between items-center p-4">
          <h1 className="text-xl font-bold">Employer Dashboard</h1>
          <nav className="space-x-4">
            <a href="/" className="hover:text-blue-300">Home</a>
            <a href="/jobs" className="hover:text-blue-300">Jobs</a>
            <a href="/profile" className="hover:text-blue-300">Profile</a>
          </nav>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-1 pt-16 pb-12 overflow-y-auto">
        <div className="max-w-4xl mx-auto px-4">
          <JobPostingForm />
          <JobListingManager />
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-blue-900 text-white text-center p-4 fixed bottom-0 w-full">
        <p>Contact us: contact@employer.com | © 2023 Company Name</p>
        <div>
          <a href="/privacy" className="hover:text-blue-300">Privacy Policy</a> | 
          <a href="/terms" className="hover:text-blue-300"> Terms of Service</a>
        </div>
      </footer>
    </div>
  );
}

export default EmployerDashboard;