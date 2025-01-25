import { ReactSVG } from 'react-svg';
import {
  Dialog,
  DialogContent,
  DialogTitle,
  DialogTrigger,
} from '@/components/ui/dialog';

export function FlagSVG({
  svgString,
  className,
  size = '1rem',
  allowExpand = false,
}) {
  if (!svgString) return null;

  // Extract width and height from SVG string if they exist
  const widthMatch = svgString.match(/width="(\d+)"/);
  const heightMatch = svgString.match(/height="(\d+)"/);
  const width = widthMatch ? parseInt(widthMatch[1]) : 24;
  const height = heightMatch ? parseInt(heightMatch[1]) : 24;

  const modifiedSvgString = svgString
    .replace(/x2="([\-\w]+) y1="([\-\w]+)"/g, 'x2="$1" y2="$2"')
    .replace(/<!-- ([\w\s]+) \*\//g, '<!-- $1 -->')
    .replace(/(<svg[^>]*)>/, (match, p1) => {
      const cleanedAttributes = p1.replace(/viewBox="[^"]*"/, '');
      return `${cleanedAttributes} viewBox="0 0 ${width} ${height}">`;
    });

  // Add safety check before creating Blob
  if (!modifiedSvgString.includes('</svg>')) {
    console.warn('Invalid SVG string detected');
    return null;
  }

  const svgBlob = new Blob([modifiedSvgString], { type: 'image/svg+xml' });
  const url = URL.createObjectURL(svgBlob);

  const SvgComponent = (
    <ReactSVG
      src={url}
      wrapper="span"
      className={className}
      onLoad={() => URL.revokeObjectURL(url)}
      beforeInjection={(svg) => {
        svg.removeAttribute('width');
        svg.removeAttribute('height');
        svg.setAttribute('preserveAspectRatio', 'xMidYMid meet');
        svg.style.height = size;
        svg.style.width = 'auto';
        svg.style.display = 'inline-block';
        svg.style.verticalAlign = 'middle';
      }}
    />
  );

  if (!allowExpand) {
    return SvgComponent;
  }

  return (
    <Dialog>
      <DialogTrigger asChild>
        <div className="cursor-pointer">{SvgComponent}</div>
      </DialogTrigger>
      <DialogContent className="max-w-[90vw] max-h-[90vh]">
        <DialogTitle className="mb-4">Flag</DialogTitle>
        <ReactSVG
          src={url}
          wrapper="span"
          className="w-full h-full"
          onLoad={() => URL.revokeObjectURL(url)}
          beforeInjection={(svg) => {
            svg.removeAttribute('width');
            svg.removeAttribute('height');
            svg.setAttribute('preserveAspectRatio', 'xMidYMid meet');
            svg.style.maxWidth = '100%';
            svg.style.width = 'auto';
            svg.style.maxHeight = '80vh';
            svg.style.height = 'auto';
            svg.style.display = 'block';
            svg.style.margin = 'auto';
          }}
        />
      </DialogContent>
    </Dialog>
  );
}
