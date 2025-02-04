'use client';

import { DashboardNav } from '@/components/nav';
import { Avatar, AvatarFallback } from '@/components/ui/avatar';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from '@/components/ui/tooltip';
import { useUser } from '@/context/user-context';
import { PlusCircleIcon } from 'lucide-react';

export default function AccountPage() {
  const { user } = useUser();

  if (!user) return null;

  const handleBuyCredits = () => {
    if (!user?.email || user?.email.startsWith('user')) {
      if (
        !confirm(
          'It is strongly recommended to set an email address for account recovery before making purchases. Click OK to proceed anyway, or Cancel to create a new account with your email.'
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

  return (
    <div className="flex min-h-screen flex-col">
      <DashboardNav />
      <main className="flex-1 px-4">
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
                  <p className="text-sm text-muted-foreground">{user.email}</p>
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
                  <Tooltip>
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
                      <p>Click here to purchase more credits!</p>
                    </TooltipContent>
                  </Tooltip>
                </TooltipProvider>
              </div>
            </CardContent>
          </Card>
        </div>
      </main>
    </div>
  );
}
