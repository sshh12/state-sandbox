'use client';

import ReactMarkdown from 'react-markdown';
import { Dialog, DialogContent, DialogTitle } from '@/components/ui/dialog';

export function ReportDialog({ isOpen, onOpenChange, report }) {
  if (!report) return null;

  return (
    <Dialog
      open={isOpen}
      onOpenChange={(open) => {
        if (open === false) {
          onOpenChange(false);
        }
      }}
      onPointerDownOutside={(e) => {
        e.preventDefault();
      }}
    >
      <DialogContent className="max-w-[95vw] max-h-[80vh] overflow-y-auto">
        <DialogTitle className="sr-only">Report</DialogTitle>
        <div className="prose prose-sm dark:prose-invert max-w-[65ch] mx-auto">
          <ReactMarkdown>{report}</ReactMarkdown>
        </div>
      </DialogContent>
    </Dialog>
  );
}
