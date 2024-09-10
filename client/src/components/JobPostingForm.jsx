import React, { useState } from 'react';

const JobPostingForm = ({ postJobHandler }) => {
  const [formData, setFormData] = useState({
    title: '',
    description: '',
    requirements: '',
    location: '',
    jobType: '',
    applicationDeadline: '',
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    if (Object.values(formData).some(field => field.trim() === '')) {
      setError('All fields are required.');
      return;
    }

    setLoading(true);
    try {
      await postJobHandler(formData);
      // Optionally reset form after submission
      setFormData({
        title: '',
        description: '',
        requirements: '',
        location: '',
        jobType: '',
        applicationDeadline: '',
      });
    } catch (err) {
      setError('Error submitting form. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-md mx-auto my-8 bg-white p-5 rounded shadow">
      <form onSubmit={handleSubmit} aria-label="Job Posting Form">
        <div className="mb-4">
          <label className="block text-sm font-medium mb-1" htmlFor="title">Job Title</label>
          <input
            type="text"
            id="title"
            name="title"
            value={formData.title}
            onChange={handleChange}
            className="w-full p-2 border border-gray-300 rounded"
            aria-label="Job Title"
            role="textbox"
          />
        </div>

        <div className="mb-4">
          <label className="block text-sm font-medium mb-1" htmlFor="description">Description</label>
          <textarea
            id="description"
            name="description"
            value={formData.description}
            onChange={handleChange}
            className="w-full p-2 border border-gray-300 rounded"
            aria-label="Job Description"
            role="textbox"
          />
        </div>

        <div className="mb-4">
          <label className="block text-sm font-medium mb-1" htmlFor="requirements">Requirements</label>
          <textarea
            id="requirements"
            name="requirements"
            value={formData.requirements}
            onChange={handleChange}
            className="w-full p-2 border border-gray-300 rounded"
            aria-label="Job Requirements"
            role="textbox"
          />
        </div>

        <div className="mb-4">
          <label className="block text-sm font-medium mb-1" htmlFor="location">Location</label>
          <input
            type="text"
            id="location"
            name="location"
            value={formData.location}
            onChange={handleChange}
            className="w-full p-2 border border-gray-300 rounded"
            aria-label="Job Location"
            role="textbox"
          />
        </div>

        <div className="mb-4">
          <label className="block text-sm font-medium mb-1" htmlFor="jobType">Job Type</label>
          <input
            type="text"
            id="jobType"
            name="jobType"
            value={formData.jobType}
            onChange={handleChange}
            className="w-full p-2 border border-gray-300 rounded"
            aria-label="Job Type"
            role="textbox"
          />
        </div>

        <div className="mb-4">
          <label className="block text-sm font-medium mb-1" htmlFor="applicationDeadline">Application Deadline</label>
          <input
            type="date"
            id="applicationDeadline"
            name="applicationDeadline"
            value={formData.applicationDeadline}
            onChange={handleChange}
            className="w-full p-2 border border-gray-300 rounded"
            aria-label="Application Deadline"
            role="textbox"
          />
        </div>

        {error && <p className="text-red-500 text-sm">{error}</p>}

        <button
          type="submit"
          disabled={loading}
          className={`mt-4 w-full p-2 text-white rounded ${loading ? 'bg-gray-400' : 'bg-[#340487] hover:bg-[#5b3caa]'}`}
          aria-label="Submit"
          role="button"
        >
          {loading ? 'Submitting...' : 'Submit'}
        </button>
      </form>
    </div>
  );
};

export default JobPostingForm;