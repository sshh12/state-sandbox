'use client';

import { useUser } from '@/context/user-context';
import { useRouter } from 'next/navigation';
import { useEffect } from 'react';
import { Spinner } from '@/components/ui/spinner';

export default function Home() {
  const router = useRouter();
  const { user, states, loading } = useUser();

  useEffect(() => {
    if (!loading && user === null) {
      router.push('/auth');
    }
  }, [user, router, loading]);

  useEffect(() => {
    if (states !== null && states.length === 0) {
      router.push('/new-state');
    } else if (states !== null && states.length > 0) {
      router.push(`/state/${states.at(-1).id}`);
    }
  }, [states, router]);

  return (
    <div className="h-screen w-full flex items-center justify-center">
      <Spinner className="h-8 w-8" />
    </div>
  );
}
