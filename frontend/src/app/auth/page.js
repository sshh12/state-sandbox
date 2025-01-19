'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { Input } from '@/components/ui/input';
import { Button } from '@/components/ui/button';
import { useToast } from '@/hooks/use-toast';
import { useUser } from '@/context/user-context';
import { WhatIsThisModal } from '@/components/WhatIsThisModal';

export default function AuthPage() {
  const [email, setEmail] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const router = useRouter();
  const { toast } = useToast();
  const { createAccount } = useUser();
  const [isModalOpen, setIsModalOpen] = useState(false);

  const generateTempEmail = (username) => {
    return `${username}@state.sshh.io`;
  };

  const isValidEmail = (email) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  };

  const generateRandomUsername = () => {
    return `user${Math.floor(Math.random() * 1000000)}`;
  };

  const handleCreateTempAccount = async () => {
    const username = generateRandomUsername();
    const finalEmail = generateTempEmail(username);

    try {
      setIsLoading(true);
      await createAccount(username, finalEmail);
      toast({
        title: 'Success!',
        description: 'Temporary account created successfully',
      });
      router.push('/new-state');
    } catch (error) {
      toast({
        title: 'Error',
        description: error.message,
        variant: 'destructive',
      });
    } finally {
      setIsLoading(false);
    }
  };

  const handleCreateRegularAccount = async () => {
    if (!email.trim() || !isValidEmail(email)) {
      toast({
        title: 'Invalid Input',
        description: 'Please enter a valid email address',
        variant: 'destructive',
      });
      return;
    }

    try {
      setIsLoading(true);
      const username = email.split('@')[0];
      await createAccount(username, email);
      toast({
        title: 'Success!',
        description: 'Account created successfully',
      });
      router.push('/new-state');
    } catch (error) {
      if (error.message.includes('login link')) {
        toast({
          title: 'Check Your Email',
          description: error.message,
        });
      } else {
        toast({
          title: 'Error',
          description: error.message,
          variant: 'destructive',
        });
      }
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && email.trim()) {
      handleCreateRegularAccount();
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-background">
      <div className="w-full max-w-md space-y-6 p-6">
        <div className="space-y-2 text-center">
          <h1 className="text-3xl font-bold">State Sandbox</h1>
          <p className="text-muted-foreground">
            Enter your email to start building. This tool is experimental and
            projects may be deleted without notice.
          </p>
          <Button
            variant="ghost"
            size="sm"
            onClick={() => setIsModalOpen(true)}
          >
            What is this?
          </Button>
        </div>

        <div className="space-y-4">
          <Input
            placeholder="Enter email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            onKeyPress={handleKeyPress}
            disabled={isLoading}
            autoFocus
          />
          <div className="flex flex-col gap-2">
            <Button
              className="w-full"
              onClick={handleCreateRegularAccount}
              disabled={!email.trim() || isLoading}
            >
              {isLoading ? 'Creating Account...' : 'Create Account (or login)'}
            </Button>
            <Button
              className="w-full"
              variant="outline"
              onClick={handleCreateTempAccount}
              disabled={isLoading}
            >
              Create Temporary Account
            </Button>
          </div>
        </div>
      </div>

      <WhatIsThisModal
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
      />
    </div>
  );
}
