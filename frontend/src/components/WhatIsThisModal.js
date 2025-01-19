'use client';

import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from '@/components/ui/dialog';

export function WhatIsThisModal({ isOpen, onClose }) {
  return (
    <Dialog open={isOpen} onOpenChange={onClose}>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>About State Sandbox</DialogTitle>
          <DialogDescription className="space-y-4 pt-4">
            <p>
              State Sandbox is an experimental AI-powered simulation tool that
              lets you explore different policy decisions and their impacts on a
              simulated society.
            </p>
            <p>
              Create a state, set policies, and watch how your decisions affect
              various aspects of society including the economy, social welfare,
              environment, and more.
            </p>
            <p>
              This is a research project and experimental tool. Data may be
              deleted without notice. Use a temporary account to try it out, or
              create a regular account to save your progress.
            </p>
          </DialogDescription>
        </DialogHeader>
      </DialogContent>
    </Dialog>
  );
}
