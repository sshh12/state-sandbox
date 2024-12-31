'use client';

import { useParams } from 'next/navigation';
import StatePage from '../page';

export default function StateWorkspace() {
  const params = useParams();

  return <StatePage stateId={params.stateId} />;
}
