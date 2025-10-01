interface RatingStarsProps {
  rating: number;
}

export default function RatingStars({ rating }: RatingStarsProps) {
  return (
    <div className="flex space-x-1 mt-2">
      {Array.from({ length: 5 }).map((_, index) => (
        <span
          key={index}
          className={index < rating ? "text-yellow-400" : "text-gray-300"}
        >
          ★
        </span>
      ))}
    </div>
  );
}
