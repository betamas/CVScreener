CV_SCREENING_PROMPT = """
Assess how a person is qualified for [an O-1A immigration visa](https://www.uscis.gov/working-in-the-united-states/temporary-workers/o-1-visa-individuals-with-extraordinary-ability-or-achievement). There are 8 criterion defined in O-1A (you can find more info about those criterion by opening [this link](https://www.uscis.gov/policy-manual/volume-2-part-m#), clicking on the Appendices and expand the section of “Appendix: Satisfying the O-1A Evidentiary Requirements”)

- Awards - Documentation of the beneficiary's receipt of nationally or internationally recognized prizes or awards for excellence in the field of endeavor.
- Membership - Documentation of the beneficiary's membership in associations in the field for which classification is sought, which require outstanding achievements of their members, as judged by recognized national or international experts in their disciplines or fields.
- Press - Published material in professional or major trade publications or major media about the beneficiary, relating to the beneficiary's work in the field for which classification is sought. This evidence must include the title, date, and author of such published material and any necessary translation.
- Judging - Evidence of the beneficiary's participation on a panel, or individually, as a judge of the work of others in the same or in an allied field of specialization for which classification is sought.
- Original contribution - Evidence of the beneficiary's original scientific, scholarly, or business-related contributions of major significance in the field.
- Scholarly articles - Evidence of the beneficiary's authorship of scholarly articles in the field, in professional journals, or other major media.
- Critical employment - Evidence that the beneficiary has been employed in a critical or essential capacity for organizations and establishments that have a distinguished reputation.
- High remuneration - Evidence that the beneficiary has either commanded a high salary or will command a high salary or other remuneration for services as evidenced by contracts or other reliable evidence.

This rough assessment is usually done using a person's CV and the expectation is to produce two things, 

- Give a rating (low, medium & high) on the chance that this person is qualified for an O-1A immigration visa
- List all the things that the person has done and meet the 8 criterion of O-1A


CV: {text}
Overall Rating (low, medium, or high): """