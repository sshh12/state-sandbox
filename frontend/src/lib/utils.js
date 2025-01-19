import { clsx } from 'clsx';
import { twMerge } from 'tailwind-merge';

export function cn(...inputs) {
  return twMerge(clsx(inputs));
}

export function getValue(snapshot, metric) {
  if (!snapshot || !metric) return '';
  const metricParts = metric.split('.');
  const metricValue = metricParts.reduce((acc, part) => acc[part], snapshot);
  return metricValue;
}

export function formatValue(snapshot, metric) {
  if (!snapshot || !metric) return '';
  const metricValue = getValue(snapshot, metric);
  const { value, unit } = metricValue;
  if (unit === 'USD') {
    return value.toLocaleString(undefined, {
      style: 'currency',
      currency: 'USD',
    });
  } else if (unit === '%') {
    return `${Math.round(value * 100)}%`;
  } else if (!!unit) {
    return value.toLocaleString(undefined, {
      style: 'decimal',
      maximumFractionDigits: 2,
    });
  }
  return value;
}

export function formatNumber(value) {
  if (value >= 1e9) {
    return `${(value / 1e9).toFixed(1)}B`;
  } else if (value >= 1e6) {
    return `${(value / 1e6).toFixed(1)}M`;
  } else if (value >= 1e3) {
    return `${(value / 1e3).toFixed(1)}K`;
  }
  return value.toLocaleString();
}

export function formatDiff(snapshotA, snapshotB, metric) {
  if (!snapshotA || !snapshotB || !metric) return '0%';
  const metricA = getValue(snapshotA, metric);
  const metricB = getValue(snapshotB, metric);
  const percentDiff = ((metricB.value - metricA.value) / metricA.value) * 100;
  return `${percentDiff >= 0 ? '+' : ''}${percentDiff.toFixed(2)}%`;
}

export function formatMonthDate(date) {
  return new Date(date + 'T00:00:00').toLocaleDateString('en-US', {
    month: 'short',
    year: 'numeric',
  });
}
export function formatYearDate(date, offset = 0) {
  const dateObj = new Date(date + 'T00:00:00');
  dateObj.setFullYear(dateObj.getFullYear() + offset);
  return dateObj.toLocaleDateString('en-US', {
    year: 'numeric',
  });
}
