'use client';

import { createContext, useContext, useEffect, useState } from 'react';
import { api } from '@/lib/api';

const UserContext = createContext({
  user: null,
  states: null,
  refreshUser: async () => {},
  refreshStates: async () => {},
});

export function UserProvider({ children }) {
  const [user, setUser] = useState(null);
  const [states, setStates] = useState(null);

  useEffect(() => {
    if (localStorage.getItem('state-sandbox-token')) {
      api
        .getCurrentUser()
        .then(setUser)
        .then(fetchData)
        .catch((e) => {
          if (e.message.includes('token')) {
            localStorage.removeItem('state-sandbox-token');
            window.location.href = '/';
          }
        });
    } else {
      api.createAccount().then(setUser).then(fetchData);
    }
  }, []);

  const refreshUser = async () => {
    const user = await api.getCurrentUser();
    setUser(user);
  };

  const fetchData = async () => {
    await refreshStates();
  };

  const refreshStates = async () => {
    const states = await api.getStates();
    setStates(states);
  };

  return (
    <UserContext.Provider
      value={{
        user,
        states,
        refreshUser,
        refreshStates,
      }}
    >
      {children}
    </UserContext.Provider>
  );
}

export const useUser = () => useContext(UserContext);
