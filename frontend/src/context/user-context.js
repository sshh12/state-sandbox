'use client';

import { createContext, useContext, useEffect, useState } from 'react';
import { api } from '@/lib/api';

const UserContext = createContext({
  user: null,
  refreshUser: async () => {},
});

export function UserProvider({ children }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    if (localStorage.getItem('token')) {
      api
        .getCurrentUser()
        .then(setUser)
        .catch((e) => {
          if (e.message.includes('token')) {
            localStorage.removeItem('token');
            window.location.href = '/';
          }
        });
    }
  }, []);

  const refreshUser = async () => {
    const user = await api.getCurrentUser();
    setUser(user);
  };

  return (
    <UserContext.Provider
      value={{
        user,
        refreshUser,
      }}
    >
      {children}
    </UserContext.Provider>
  );
}

export const useUser = () => useContext(UserContext);
