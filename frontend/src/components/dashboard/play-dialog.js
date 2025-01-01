'use client';

import { useState } from 'react';
import { Button } from '@/components/ui/button';
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from '@/components/ui/dialog';
import { Textarea } from '@/components/ui/textarea';

export function PlayDialog({ date }) {
  const [policies, setPolicies] = useState('');
  const [advisorFeedback, setAdvisorFeedback] = useState('');

  const getAdvisorFeedback = (type) => {
    // TODO: Implement advisor feedback API calls
    setAdvisorFeedback(`${type} advisor feedback will appear here...`);
  };

  const handlePlay = () => {
    // TODO: Implement play functionality
    console.log('Playing with policies:', policies);
  };

  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button className="bg-black text-white">
          Play (
          {date
            ? new Date(date + 'T00:00:00').toLocaleDateString('en-US', {
                month: 'short',
                year: 'numeric',
              })
            : null}
          )
        </Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-[600px]">
        <DialogHeader>
          <DialogTitle>Play Turn</DialogTitle>
          <DialogDescription>
            Set your policies and get advice from your advisors before advancing
            the simulation.
          </DialogDescription>
        </DialogHeader>
        <div className="grid gap-4 py-4">
          <div className="space-y-2">
            <h4 className="font-medium">Custom Policies</h4>
            <Textarea
              placeholder="Enter your policy changes here..."
              value={policies}
              onChange={(e) => setPolicies(e.target.value)}
              className="h-32"
            />
          </div>
          <div className="space-y-2">
            <h4 className="font-medium">Advisor Feedback</h4>
            <div className="flex gap-2">
              <Button
                variant="outline"
                onClick={() => getAdvisorFeedback('Economic')}
              >
                Economic Advisor
              </Button>
              <Button
                variant="outline"
                onClick={() => getAdvisorFeedback('Government')}
              >
                Government Advisor
              </Button>
              <Button
                variant="outline"
                onClick={() => getAdvisorFeedback('Cultural')}
              >
                Cultural Advisor
              </Button>
            </div>
            {advisorFeedback && (
              <div className="mt-2 rounded-md bg-muted p-4 text-sm">
                {advisorFeedback}
              </div>
            )}
          </div>
        </div>
        <DialogFooter>
          <Button onClick={handlePlay}>Play</Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}
