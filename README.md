This Python script calculates the expected value of drafting events on Magic: The Gagther Arena. For each event, and for each win percentage, it computes the probability of each possible win record. From these probabilities it calculates the expected value of each event. The Reddit post with my conclusions is here: https://www.reddit.com/r/MagicArena/comments/g2nt1v/expected_value_of_all_arena_draft_events_compared/

Insights:
1.	Look at the green lines if building your collection for standard matters to you, and look at the yellow lines if you’re more concerned with the cost in dollars for each draft and whether you can go infinite.
2.	If your win rate is around 50% (most people), and packs matter to you, the average reward (if you play enough games) is the same across all three events. Let the format (bot or player; best-of-three matches) guide your decision. This assumes your win % will be the same across events.
3.	If your win rate is around 50% (most people), and packs don’t matter to you (you just want to draft as much as you can for the cheapest price), you’re much better off with ranked draft. You’ll lose ~600 gems less on average per draft! Premier vs. traditional doesn’t make a difference.
4.	The point at which you break even (blue line) is very similar for each draft event. Just considering gems, traditional is a bit better than the others (e.g., you need to win ~3% more of your games in traditional, and ~8% of your games in ranked, compared to premium, to break even)
5.	For ranked, you’ll lose less value if you’re bad and win less value if you’re good, relative to the other draft events. If packs matter to you, a 52% winrate is parity; you need to consider if you’re better or worse than that to choose whether to draft the other events. If only gems matter, you have to be very good with a win rate ~61% to not lose more from premium and traditional (but you’re stuck drafting with bots in ranked).
6.	For the competitive player who is good and is only concerned with gems/drafting, after ~56% traditional starts to provide more value than premier the greater and greater the win % is.
Draft event descriptions:
•	Premier draft: people; 1500 Gems (or 10,000 Gold) entry fee; 7 wins or 3 losses; ranked
•	Traditional draft: people; 1500 Gems (or 10,000 Gold) entry fee; three best of three matches (regardless of win/loss record); not ranked
•	Ranked draft: bots; 750 Gems (or 5,000 Gold) entry fee; 7 wins or 3 losses; ranked
Notes:
1.	Only gem entry fee is used (not gold entry fee).
2.	The value of cards drafted for your collection is not considered.
3.	The calculations take into account the difference between game vs. match win rate for the traditional draft event.
4.	The method relies heavily on this article from Frank Karsten (https://www.channelfireball.com/all-strategy/articles/whats-the-best-mtg-arena-event-for-expected-value-and-can-you-go-infinite/)

