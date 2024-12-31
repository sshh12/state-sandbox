'use client';

import { useUser } from '@/context/user-context';
import { useRouter } from 'next/navigation';

export default function Home() {
  const router = useRouter();
  const { user, states } = useUser();

  if (states !== null && states.length == 0) {
    router.push('/new-state');
  }

  return (
    <div>
      <h1>State Sandbox</h1>
      <p>Welcome, {user?.username}</p>
    </div>
  );
}
