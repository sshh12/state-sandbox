'use client';

import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { cn } from '@/lib/utils';
import { useState, useMemo, useEffect } from 'react';
import { api } from '@/lib/api';
import { useRouter } from 'next/navigation';
import { ProgressTimer } from '@/components/ui/progress-timer';
import { useUser } from '@/context/user-context';
import Image from 'next/image';

const questions = [
  'Individual rights should take precedence over collective needs',
  'The state should have a strong role in economic affairs',
  'Scientific progress should be prioritized over traditional values',
  'International cooperation is more important than national sovereignty',
  'The state should promote traditional cultural values',
  'Economic inequality is acceptable for societal progress',
  'Personal freedom can be limited for social stability',
  'Economic growth should take priority over resource conservation',
  'The state should provide comprehensive social welfare',
  'Private enterprises should operate with minimal regulation',
  'Education should focus on practical skills over theoretical knowledge',
  'Healthcare should be market-driven rather than state-provided',
  'Citizens have a duty to serve their country',
  'Environmental protection should take priority over economic growth',
  'Society should be open to cultural change and immigration',
  'Religious values should guide public policy',
  'Justice should prioritize rehabilitation over punishment',
  'Technological innovation should be closely regulated',
  'Media should operate independently of government influence',
  'Power should be decentralized to local communities',
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
  const { refreshStates } = useUser();
  const [ratings, setRatings] = useState({});
  const [countryName, setCountryName] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [loadingMessageIndex, setLoadingMessageIndex] = useState(0);
  const [showAllQuestions, setShowAllQuestions] = useState(false);
  const [shuffledQuestions, setShuffledQuestions] = useState(questions);
  const router = useRouter();

  useEffect(() => {
    setShuffledQuestions([...questions].sort(() => Math.random() - 0.5));
  }, []);

  const visibleQuestions = showAllQuestions
    ? shuffledQuestions
    : shuffledQuestions.slice(0, 5);

  const isFormValid = useMemo(() => {
    return countryName.trim() !== '' && Object.keys(ratings).length >= 5;
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
      const questionData = visibleQuestions
        .filter(
          (_, index) => ratings[index] !== undefined && ratings[index] !== null
        )
        .map((question, index) => ({
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
            refreshStates().then(() => {
              router.push(`/state/${stateId}?showInfo=true`);
            });
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

            {visibleQuestions.map((question, index) => (
              <div key={index} className="space-y-3">
                <Label className="block text-base">
                  {question}
                  {index < 5 && <span className="text-red-500 ml-1">*</span>}
                </Label>
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

            {!showAllQuestions && (
              <div className="space-y-2">
                <div className="h-px bg-border" />
                <p className="text-sm text-muted-foreground text-center">
                  Want to further customize your nation? Answer more optional
                  questions below.
                </p>
                <Button
                  type="button"
                  variant="outline"
                  className="w-full"
                  onClick={() => setShowAllQuestions(true)}
                >
                  Show {shuffledQuestions.length - 5} More Optional Questions
                </Button>
              </div>
            )}

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
                  duration={100000}
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
      <div className="hidden lg:block flex-1 bg-black relative">
        <Image
          src="/greece.jpg"
          alt="https://unsplash.com/photos/low-angle-photography-of-the-parthenon-greece-DELDTYAjPrg"
          fill
          className="object-cover"
          priority
        />
      </div>
    </div>
  );
}
