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
import { ProgressTimer } from '@/components/ui/progress-timer';
import { formatMonthDate } from '@/lib/utils';
import { api } from '@/lib/api';
import ReactMarkdown from 'react-markdown';

export function PlayDialog({ date, onPlay, turnLoading, stateId }) {
  const [policies, setPolicies] = useState('');
  const [advisorFeedback, setAdvisorFeedback] = useState('');
  const [isOpen, setIsOpen] = useState(false);
  const [customQuestion, setCustomQuestion] = useState('');
  const [advisorLoading, setAdvisorLoading] = useState(false);

  const advisorQuestions = [
    'How can I increase GDP?',
    'How can I improve public approval?',
  ];

  const getAdvisorFeedback = async (type) => {
    setAdvisorLoading(true);
    try {
      const advice = await api.getStateAdvice(stateId, type);
      setAdvisorFeedback(advice.markdown_advice);
    } finally {
      setAdvisorLoading(false);
    }
  };

  const handlePlay = () => {
    setAdvisorFeedback('');
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
            <>Play ({date ? formatMonthDate(date) : null})</>
          )}
        </Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-[600px]">
        <DialogHeader>
          <DialogTitle>Play Turn</DialogTitle>
          <DialogDescription>
            Set your policies (if any) and get advice from your advisors before
            advancing the simulation by exactly one month.
          </DialogDescription>
        </DialogHeader>
        <div className="grid gap-4 py-4">
          {turnLoading && (
            <ProgressTimer
              isRunning={turnLoading}
              duration={5 * 60 * 1000}
              className="w-full"
            />
          )}
          <div className="space-y-2">
            <h4 className="font-medium">Your Policies</h4>
            <Textarea
              placeholder="Enter your policy changes here..."
              value={policies}
              onChange={(e) => setPolicies(e.target.value)}
              className="h-32"
              disabled={turnLoading}
            />
          </div>
          <div className="space-y-2">
            <h4 className="font-medium">Ask Advisors</h4>
            <div className="flex flex-col gap-2">
              {advisorQuestions.map((question, index) => (
                <Badge
                  key={index}
                  variant="outline"
                  className={`p-2 cursor-pointer w-full text-left ${
                    advisorLoading || turnLoading
                      ? 'opacity-50 cursor-not-allowed'
                      : 'hover:bg-secondary'
                  }`}
                  onClick={() =>
                    !advisorLoading &&
                    !turnLoading &&
                    getAdvisorFeedback(question)
                  }
                >
                  {question}
                </Badge>
              ))}
              <div className="flex gap-2">
                <Input
                  placeholder="Ask your own question..."
                  value={customQuestion}
                  onChange={(e) => setCustomQuestion(e.target.value)}
                  disabled={advisorLoading || turnLoading}
                  onKeyDown={(e) => {
                    if (
                      e.key === 'Enter' &&
                      customQuestion.trim() &&
                      !advisorLoading &&
                      !turnLoading
                    ) {
                      getAdvisorFeedback(customQuestion);
                    }
                  }}
                />
                <Button
                  variant="outline"
                  className="shrink-0"
                  disabled={advisorLoading || turnLoading}
                  onClick={() => {
                    if (customQuestion.trim()) {
                      getAdvisorFeedback(customQuestion);
                    }
                  }}
                >
                  {advisorLoading ? (
                    <Loader2 className="h-4 w-4 animate-spin" />
                  ) : (
                    'Ask'
                  )}
                </Button>
              </div>
            </div>
            {advisorFeedback && (
              <div className="mt-2 rounded-md bg-muted p-4 text-sm prose prose-sm max-w-none max-h-[200px] overflow-y-auto">
                <ReactMarkdown>{advisorFeedback}</ReactMarkdown>
              </div>
            )}
          </div>
        </div>
        <DialogFooter>
          <Button onClick={handlePlay} disabled={turnLoading || advisorLoading}>
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
