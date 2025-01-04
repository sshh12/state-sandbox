'use client';

import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { cn } from '@/lib/utils';
import { useState, useMemo, useEffect } from 'react';
import { api } from '@/lib/api';
import { useRouter } from 'next/navigation';
import { ProgressTimer } from '@/components/ui/progress-timer';

const questions = [
  'Individual rights should take precedence over collective security',
  'The state should own and operate key industries and utilities',
  'Scientific research should be prioritized over traditional values',
  'International cooperation is more important than national sovereignty',
  'The state should enforce traditional cultural and moral values',
  'Economic inequality is acceptable if it drives innovation and growth',
  'Civil liberties can be restricted to maintain social order',
  'Natural resources should be exploited to maximize economic output',
  'The state should provide universal basic income to all citizens',
  'Technology companies should be allowed to self-regulate',
];

const ratingOptions = [
  {
    value: '1',
    label: 'Strongly Disagree',
    color: 'bg-red-700 hover:bg-red-800',
  },
  { value: '2', label: 'Disagree', color: 'bg-red-500 hover:bg-red-600' },
  { value: '3', label: 'Neutral', color: 'bg-gray-500 hover:bg-gray-600' },
  { value: '4', label: 'Agree', color: 'bg-green-500 hover:bg-green-600' },
  {
    value: '5',
    label: 'Strongly Agree',
    color: 'bg-green-700 hover:bg-green-800',
  },
];

const loadingMessages = [
  'Designing the flag...',
  'Recruiting an army...',
  'Establishing government...',
  'Writing the constitution...',
  'Building infrastructure...',
  'Training diplomats...',
  'Setting up the economy...',
  'Founding the capital city...',
  'Minting currency...',
  'Creating national parks...',
  'Composing national anthem...',
  'Establishing time zones...',
  'Drawing border lines...',
  'Setting up postal service...',
  'Designing official seals...',
  'Planting national tree...',
  'Choosing national bird...',
  'Building parliament...',
  'Training civil servants...',
  'Establishing courts...',
];

export default function NewState() {
  const [ratings, setRatings] = useState({});
  const [countryName, setCountryName] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [loadingMessageIndex, setLoadingMessageIndex] = useState(0);
  const router = useRouter();

  const isFormValid = useMemo(() => {
    return (
      countryName.trim() !== '' &&
      Object.keys(ratings).length === questions.length
    );
  }, [countryName, ratings]);

  useEffect(() => {
    let interval;
    if (isLoading) {
      interval = setInterval(() => {
        setLoadingMessageIndex((prev) => (prev + 1) % loadingMessages.length);
      }, 3000); // Change message every 2 seconds
    }
    return () => clearInterval(interval);
  }, [isLoading]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!isFormValid) return;

    setIsLoading(true);
    try {
      const questionData = questions.map((question, index) => ({
        question,
        value: parseInt(ratings[index]),
      }));

      let stateId = null;
      await api.createState(countryName, questionData, (event) => {
        switch (event.type) {
          case 'state_created':
            stateId = event.id;
            break;
          case 'status':
            break;
          case 'complete':
            router.push(`/state/${stateId}`);
            break;
        }
      });
    } catch (error) {
      console.error('Failed to create state:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleRatingClick = (questionIndex, value) => {
    setRatings((prev) => ({
      ...prev,
      [questionIndex]: value,
    }));
  };

  return (
    <div className="min-h-screen flex flex-col lg:flex-row">
      {/* Left Panel with Form */}
      <div className="flex-1 p-4 lg:p-10 w-full">
        <div className="max-w-full lg:max-w-[800px] mx-auto">
          <h1 className="text-xl lg:text-2xl font-semibold mb-2">
            Found a Nation
          </h1>
          <p className="text-muted-foreground mb-4">
            Your choices will influence the nation's policies, structure, and
            more. After creation, you will be able to change almost{' '}
            <i>anything</i> by passing new laws and policies.
          </p>
          <p className="text-sm text-muted-foreground mb-8 italic">
            Disclaimer: States Sandbox is a Large Language Model-based
            simulation and does not reflect real-world governance. The outcomes
            are influenced by the biases present in our prompts and underlying
            AI models, and should not be taken as realistic predictions. The
            game and many of it's characteristics are inspired by{' '}
            <a href="https://nationstates.net">NationStates</a>.
          </p>

          <form onSubmit={handleSubmit} className="space-y-6">
            <div className="space-y-3">
              <Label htmlFor="country">Country Name</Label>
              <Input
                id="country"
                placeholder="Enter suggested country name"
                className="w-full"
                value={countryName}
                onChange={(e) => setCountryName(e.target.value)}
                required
              />
            </div>

            {questions.map((question, index) => (
              <div key={index} className="space-y-3">
                <Label className="block text-base">{question}</Label>
                <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-2">
                  {ratingOptions.map((option) => (
                    <Button
                      key={option.value}
                      type="button"
                      variant={
                        ratings[index] === option.value ? 'default' : 'outline'
                      }
                      className={cn(
                        'px-2 h-11',
                        ratings[index] === option.value
                          ? cn(option.color, 'text-white border-0')
                          : 'hover:bg-gray-100',
                        'text-xs sm:text-sm'
                      )}
                      onClick={() => handleRatingClick(index, option.value)}
                    >
                      {option.label}
                    </Button>
                  ))}
                </div>
              </div>
            ))}

            {!isLoading && (
              <Button
                type="submit"
                className={cn(
                  'w-full h-11 mt-8',
                  !isFormValid && 'opacity-50 cursor-not-allowed'
                )}
                disabled={!isFormValid || isLoading}
              >
                Create
              </Button>
            )}
            {isLoading && (
              <div className="mt-4">
                <ProgressTimer
                  isRunning={isLoading}
                  className="w-full"
                  duration={2 * 60 * 1000}
                />
                <p className="text-sm text-muted-foreground text-center mt-2">
                  {loadingMessages[loadingMessageIndex]}
                </p>
              </div>
            )}
          </form>
        </div>
      </div>

      {/* Right Panel */}
      <div className="hidden lg:block flex-1 bg-black" />
    </div>
  );
}
