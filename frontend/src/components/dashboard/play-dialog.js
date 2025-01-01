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
import { Badge } from '@/components/ui/badge';
import { Loader2 } from 'lucide-react';
import { Input } from '@/components/ui/input';

export function PlayDialog({ date, onPlay, turnLoading }) {
  const [policies, setPolicies] = useState('');
  const [advisorFeedback, setAdvisorFeedback] = useState('');
  const [isOpen, setIsOpen] = useState(false);
  const [customQuestion, setCustomQuestion] = useState('');

  const advisorQuestions = [
    'What policies should I implement to increase GDP?',
    'How can I improve public approval?',
    'What should I do to reduce unemployment?',
  ];

  const getAdvisorFeedback = (type) => {
    // TODO: Implement advisor feedback API calls
    setAdvisorFeedback(`${type} advisor feedback will appear here...`);
  };

  const handlePlay = () => {
    onPlay(policies);
  };

  return (
    <Dialog
      open={isOpen}
      onOpenChange={(open) => {
        // Only allow closing if not loading
        if (turnLoading && !open) return;
        setIsOpen(open);
      }}
    >
      <DialogTrigger asChild>
        <Button
          className="bg-black text-white"
          onClick={() => setIsOpen(true)}
          disabled={turnLoading}
        >
          {turnLoading ? (
            <>
              <Loader2 className="mr-2 h-4 w-4 animate-spin" />
              Simulating...
            </>
          ) : (
            <>
              Play (
              {date
                ? new Date(date + 'T00:00:00').toLocaleDateString('en-US', {
                    month: 'short',
                    year: 'numeric',
                  })
                : null}
              )
            </>
          )}
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
            <h4 className="font-medium">Your Policies</h4>
            <Textarea
              placeholder="Enter your policy changes here..."
              value={policies}
              onChange={(e) => setPolicies(e.target.value)}
              className="h-32"
            />
          </div>
          <div className="space-y-2">
            <h4 className="font-medium">Ask Advisors</h4>
            <div className="flex flex-col gap-2">
              {advisorQuestions.map((question, index) => (
                <Badge
                  key={index}
                  variant="outline"
                  className="p-2 cursor-pointer hover:bg-secondary w-full text-left"
                  onClick={() => getAdvisorFeedback(question)}
                >
                  {question}
                </Badge>
              ))}
              <div className="flex gap-2">
                <Input
                  placeholder="Ask your own question..."
                  value={customQuestion}
                  onChange={(e) => setCustomQuestion(e.target.value)}
                  onKeyDown={(e) => {
                    if (e.key === 'Enter' && customQuestion.trim()) {
                      getAdvisorFeedback(customQuestion);
                    }
                  }}
                />
                <Button
                  variant="outline"
                  className="shrink-0"
                  onClick={() => {
                    if (customQuestion.trim()) {
                      getAdvisorFeedback(customQuestion);
                    }
                  }}
                >
                  Ask
                </Button>
              </div>
            </div>
            {advisorFeedback && (
              <div className="mt-2 rounded-md bg-muted p-4 text-sm">
                {advisorFeedback}
              </div>
            )}
          </div>
        </div>
        <DialogFooter>
          <Button onClick={handlePlay} disabled={turnLoading}>
            {turnLoading ? (
              <>
                <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                Simulating...
              </>
            ) : (
              <>Play Turn</>
            )}
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}
