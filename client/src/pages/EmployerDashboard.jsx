import React from 'react';

const EmployerDashboard = () => {
  return (
    <div className="flex flex-col min-h-screen">
      {/* Fixed Header */}
      <header className="bg-gray-800 text-white p-4 sticky top-0">
        <h1 className="text-2xl">Employer Dashboard</h1>
        <nav>
          <ul className="flex space-x-4">
            <li><a href="#postings" className="hover:underline">Job Postings</a></li>
            <li><a href="#listings" className="hover:underline">Manage Listings</a></li>
            <li><a href="#about" className="hover:underline">About</a></li>
          </ul>
        </nav>
      </header>

      <div className="flex flex-col lg:flex-row flex-grow p-4">
        {/* Left Column: Job Posting Form */}
        <div className="lg:w-1/5 lg:mr-4 mb-4 lg:mb-0">
          <JobPostingForm />
        </div>

        {/* Center Column: Job Listing Manager */}
        <div className="lg:w-3/5 lg:mx-4 bg-white shadow-md p-4 rounded">
          <JobListingManager />
        </div>

        {/* Right Column: Additional Information */}
        <div className="lg:w-1/5 lg:ml-4">
          <div className="bg-white shadow-md p-4 rounded">
            {/* Placeholder for advertisements or additional info */}
            <h2 className="text-xl">Additional Information</h2>
            <p>Check out our latest updates and offers!</p>
          </div>
        </div>
      </div>
    </div>
  );
};

const JobPostingForm = () => {
  return (
    <form className="bg-white shadow-md p-4 rounded">
      <h2 className="text-xl mb-4">Post a New Job</h2>
      {/* Form Fields */}
      <input type="text" placeholder="Job Title" className="border mb-2 p-2 w-full" aria-required="true" />
      <input type="text" placeholder="Company Name" className="border mb-2 p-2 w-full" aria-required="true" />
      {/* Other form fields ... */}
      <button type="submit" className="bg-blue-500 text-white p-2 rounded mr-2">Submit</button>
      <button type="button" className="bg-gray-300 p-2 rounded">Cancel</button>
    </form>
  );
};

const JobListingManager = () => {
  return (
    <div>
      <h2 className="text-xl mb-4">Manage Job Listings</h2>
      {/* Job listings will be displayed here */}
      {/* Example listing */}
      <div className="border-b py-2 flex justify-between">
        <div>
          <h3 className="font-bold">Software Engineer</h3>
          <p>Company ABC</p>
        </div>
        <div>
          <button className="text-blue-500">Edit</button>
          <button className="text-red-500 ml-2">Delete</button>
        </div>
      </div>
      {/* More listings... */}
    </div>
  );
};

export default EmployerDashboard;