import React, { useState } from 'react';
import Auth from './components/Auth';
import TaskList from './components/TaskList';

function App() {
  const [token, setToken] = useState(localStorage.getItem('token'));

  const handleLogout = () => {
    localStorage.removeItem('token');
    setToken(null);
  };

  if (!token) {
    return <Auth onLogin={setToken} />;
  }

  return (
    <div>
      <div className="bg-gray-800 text-white p-4 flex justify-between">
        <h1 className="text-xl font-bold">Task Manager</h1>
        <button
          onClick={handleLogout}
          className="bg-red-500 px-4 py-1 rounded hover:bg-red-600"
        >
          Logout
        </button>
      </div>
      <TaskList />
    </div>
  );
}

export default App;
