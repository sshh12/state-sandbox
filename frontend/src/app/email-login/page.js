'use client';

import { useUser } from '@/context/user-context';
import { api } from '@/lib/api';
import { Loader2 } from 'lucide-react';
import { useRouter, useSearchParams } from 'next/navigation';
import { Suspense, useEffect, useState } from 'react';

function LoadingSpinner() {
  return (
    <div className="min-h-screen flex items-center justify-center">
      <div className="text-center">
        <Loader2 className="h-12 w-12 animate-spin text-primary mx-auto" />
        <p className="mt-4 text-gray-600">Logging you in...</p>
      </div>
    </div>
  );
}

function EmailLoginContent() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(true);
  const { refreshUser } = useUser();

  useEffect(() => {
    const token = searchParams.get('token');
    if (!token) {
      setError('No login token provided');
      setLoading(false);
      return;
    }

    const handleLogin = async () => {
      try {
        await api.emailLogin(token);
        window.location.href = '/';
      } catch (err) {
        setError(err.message || 'Failed to login. Please try again.');
        setLoading(false);
      }
    };

    handleLogin();
  }, [searchParams, router, refreshUser]);

  if (loading) {
    return <LoadingSpinner />;
  }

  if (error) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <div className="text-red-500 text-xl mb-4">⚠️</div>
          <h1 className="text-2xl font-bold mb-2">Login Failed</h1>
          <p className="text-gray-600 mb-4">{error}</p>
          <button
            onClick={() => router.push('/auth')}
            className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition-colors"
          >
            Back to Login
          </button>
        </div>
      </div>
    );
  }

  return null;
}

export default function EmailLoginPage() {
  return (
    <Suspense fallback={<LoadingSpinner />}>
      <EmailLoginContent />
    </Suspense>
  );
}
