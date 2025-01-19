'use client';

import { createContext, useContext, useEffect, useState } from 'react';
import { api } from '@/lib/api';
import { useRouter } from 'next/navigation';

const UserContext = createContext({
  user: null,
  states: null,
  refreshUser: async () => {},
  refreshStates: async () => {},
  createAccount: async (username, email) => {},
});

export function UserProvider({ children }) {
  const [user, setUser] = useState(null);
  const [states, setStates] = useState(null);
  const router = useRouter();

  useEffect(() => {
    if (localStorage.getItem('state-sandbox-token')) {
      api
        .getCurrentUser()
        .then(setUser)
        .then(fetchData)
        .catch((e) => {
          if (e.message.includes('token')) {
            localStorage.removeItem('state-sandbox-token');
            router.push('/auth');
          }
        });
    } else {
      router.push('/auth');
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

  const createAccount = async (username, email) => {
    const user = await api.createAccount(username, email);
    setUser(user);
    await fetchData();
    return user;
  };

  return (
    <UserContext.Provider
      value={{
        user,
        states,
        refreshUser,
        refreshStates,
        createAccount,
      }}
    >
      {children}
    </UserContext.Provider>
  );
}

export const useUser = () => useContext(UserContext);
