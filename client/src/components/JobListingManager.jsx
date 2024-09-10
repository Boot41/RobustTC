import React, { useState, useEffect } from 'react';
import axios from 'axios';

const JobListingManager = () => {
  const [jobs, setJobs] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchJobs = async () => {
      setLoading(true);
      const response = await axios.get('/api/jobs');
      setJobs(response.data);
      setLoading(false);
    };
    fetchJobs();
  }, []);

  const handleEdit = (jobId) => {
    window.location.href = `/edit/${jobId}`;
  };

  const handleDelete = async (jobId) => {
    if(window.confirm('Are you sure you want to delete this job listing?')) {
      await axios.delete(`/api/delete/job/${jobId}`);
      setJobs(jobs.filter(job => job.id !== jobId));
    }
  };

  const handleSearch = (event) => {
    setSearchQuery(event.target.value);
  };

  const filteredJobs = jobs.filter(job => job.title.toLowerCase().includes(searchQuery.toLowerCase()));

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Job Listings</h1>
      <input
        type="text"
        placeholder="Search job titles..."
        value={searchQuery}
        onChange={handleSearch}
        className="mb-4 p-2 border rounded w-full md:w-1/2"
        aria-label="Search job titles"
      />
      {loading ? (
        <div className="spinner">Loading...</div>
      ) : (
        <table className="min-w-full bg-white shadow-md rounded">
          <thead>
            <tr className="bg-gray-200">
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Title</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Location</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Date Posted</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
            </tr>
          </thead>
          <tbody>
            {filteredJobs.map((job, index) => (
              <tr key={job.id} className={`hover:shadow-lg ${index % 2 ? 'bg-gray-100' : 'bg-white'}`}>
                <td className="px-6 py-4">{job.title}</td>
                <td className="px-6 py-4">{job.location}</td>
                <td className="px-6 py-4">{new Date(job.datePosted).toLocaleDateString()}</td>
                <td className="px-6 py-4">
                  <button 
                    onClick={() => handleEdit(job.id)}
                    className="mr-2 bg-blue-500 text-white font-bold rounded p-2 hover:bg-blue-600 transition"
                    aria-label="Edit job listing"
                  >
                    Edit
                  </button>
                  <button 
                    onClick={() => handleDelete(job.id)}
                    className="bg-red-500 text-white font-bold rounded p-2 hover:bg-red-600 transition"
                    aria-label="Delete job listing"
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default JobListingManager;