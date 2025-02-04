'use client';

import { DashboardNav } from '@/components/nav';
import { Avatar, AvatarFallback } from '@/components/ui/avatar';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from '@/components/ui/tooltip';
import { useUser } from '@/context/user-context';
import { useToast } from '@/hooks/use-toast';
import { api } from '@/lib/api';
import { PlusCircleIcon } from 'lucide-react';
import { useSearchParams } from 'next/navigation';
import { Suspense, useState } from 'react';

function AccountContent() {
  const { user, refreshUser } = useUser();
  const searchParams = useSearchParams();
  const showBuyTooltip = searchParams.get('buy') === 'true';
  const [isEditingEmail, setIsEditingEmail] = useState(false);
  const [newEmail, setNewEmail] = useState('');
  const { toast } = useToast();

  const isValidEmail = (email) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  };

  if (!user) return null;

  const handleBuyCredits = () => {
    if (!user?.email || user?.email.startsWith('user')) {
      if (
        !confirm(
          'It is strongly recommended to set an email address for account recovery before making purchases. Click OK to proceed anyway, or Cancel to update your email.'
        )
      ) {
        return;
      }
    }
    window.location.href = `${
      process.env.NEXT_PUBLIC_STRIPE_LINK ||
      'https://buy.stripe.com/cN23fLbJ7gWk4ww28c'
    }?client_reference_id=statesandbox___ssuser_${user.id}`;
  };

  const handleUpdateEmail = async () => {
    if (!newEmail.trim() || !isValidEmail(newEmail)) {
      toast({
        title: 'Invalid Input',
        description: 'Please enter a valid email address',
        variant: 'destructive',
        duration: 3000,
      });
      return;
    }

    try {
      await api.updateEmail(newEmail);
      await refreshUser();
      setIsEditingEmail(false);
      toast({
        title: 'Email updated successfully',
        duration: 3000,
      });
    } catch (error) {
      toast({
        title: 'Failed to update email',
        description: error.message,
        variant: 'destructive',
        duration: 3000,
      });
    }
  };

  return (
    <div className="container py-8 space-y-8">
      <div className="flex items-center justify-between">
        <h1 className="text-3xl font-bold">Account</h1>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Profile</CardTitle>
        </CardHeader>
        <CardContent className="space-y-6">
          <div className="flex items-center space-x-4">
            <Avatar>
              <AvatarFallback>
                {user.username.slice(0, 2).toUpperCase()}
              </AvatarFallback>
            </Avatar>
            <div className="space-y-1">
              <p className="text-sm font-medium leading-none">
                {user.username}
              </p>
              {isEditingEmail ? (
                <div className="flex gap-2 items-center mt-2">
                  <Input
                    type="email"
                    value={newEmail}
                    onChange={(e) => setNewEmail(e.target.value)}
                    className="h-8"
                  />
                  <Button size="sm" onClick={handleUpdateEmail}>
                    Save
                  </Button>
                  <Button
                    size="sm"
                    variant="outline"
                    onClick={() => {
                      setIsEditingEmail(false);
                      setNewEmail(user.email || '');
                    }}
                  >
                    Cancel
                  </Button>
                </div>
              ) : (
                <div className="flex items-center gap-2">
                  <p className="text-sm text-muted-foreground">
                    {user.email || 'No email set'}
                  </p>
                  <Button
                    size="sm"
                    variant="ghost"
                    onClick={() => {
                      setIsEditingEmail(true);
                      setNewEmail(user.email || '');
                    }}
                  >
                    Edit
                  </Button>
                </div>
              )}
            </div>
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle>Credits</CardTitle>
        </CardHeader>
        <CardContent className="space-y-6">
          <div className="flex items-center gap-4">
            <div className="space-y-1">
              <p className="text-sm font-medium leading-none">
                Available Credits
              </p>
              <p className="text-2xl font-bold">{user?.credits || 0}</p>
            </div>
            <TooltipProvider>
              <Tooltip open={showBuyTooltip}>
                <TooltipTrigger asChild>
                  <Button
                    variant="secondary"
                    size="default"
                    onClick={handleBuyCredits}
                  >
                    <PlusCircleIcon className="h-4 w-4 mr-2" />
                    Buy More Credits
                  </Button>
                </TooltipTrigger>
                <TooltipContent>
                  <p>You need credits to proceed.</p>
                </TooltipContent>
              </Tooltip>
            </TooltipProvider>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}

export default function AccountPage() {
  return (
    <div className="flex min-h-screen flex-col">
      <DashboardNav />
      <main className="flex-1 px-4">
        <Suspense fallback={<div>Loading...</div>}>
          <AccountContent />
        </Suspense>
      </main>
    </div>
  );
}
