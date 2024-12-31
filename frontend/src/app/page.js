'use client';

import { useUser } from '@/context/user-context';
import { useRouter } from 'next/navigation';
import { useEffect } from 'react';

export default function Home() {
  const router = useRouter();
  const { user, states } = useUser();

  useEffect(() => {
    if (states !== null && states.length === 0) {
      router.push('/new-state');
    }
  }, [states, router]);

  return (
    <div>
      <h1>State Sandbox</h1>
      <p>Welcome, {user?.username}</p>
    </div>
  );
}
