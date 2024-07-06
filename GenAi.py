import os

import google.generativeai as genai

genai.configure(api_key=os.environ["AIzaSyAitOlDF3cNWI03Zf_bzmpoHdpKVx12AxA"])

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "What is insurance?",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Insurance is a contract, represented by a policy, in which an individual or entity (the insured) pays a premium to an insurance company (the insurer) in exchange for financial protection against potential financial losses caused by specific events. \n\nHere's a breakdown:\n\n**Key Components:**\n\n* **Risk Transfer:**  Insurance is essentially a transfer of risk from the insured to the insurer. The insured pays a premium to be protected against a specific risk, and the insurer agrees to cover the financial losses associated with that risk.\n* **Policy:**  The contract outlining the terms and conditions of the insurance agreement. It specifies the coverage, premiums, and exclusions.\n* **Premium:**  The regular payment made by the insured to the insurer for the coverage.\n* **Coverage:** The specific events, situations, or properties covered by the policy.\n* **Claim:** When the insured experiences a covered event, they can file a claim with the insurer to receive compensation for their losses.\n* **Deductible:** The amount of money the insured must pay out-of-pocket before the insurer starts covering the losses.\n\n**Types of Insurance:**\n\n* **Life Insurance:**  Provides financial protection to beneficiaries upon the death of the insured.\n* **Health Insurance:**  Covers medical expenses, such as doctor visits, hospital stays, and prescription drugs.\n* **Property Insurance:**  Protects against damage or loss to personal or business property, such as homes, vehicles, or equipment.\n* **Liability Insurance:**  Provides financial protection against lawsuits or legal claims resulting from accidents or negligence.\n* **Auto Insurance:**  Covers damage to vehicles, injuries to others, and legal expenses in the event of an accident.\n* **Business Insurance:**  Offers various coverage types for businesses, including property, liability, and worker's compensation.\n\n**Benefits of Insurance:**\n\n* **Financial Protection:**  Insurance provides a safety net against unexpected financial losses.\n* **Peace of Mind:**  Knowing you are insured can reduce anxiety and stress about potential risks.\n* **Legal Protection:**  Some types of insurance can provide legal defense and representation in the event of a claim.\n* **Spread of Risk:** Insurance companies pool together premiums from many individuals and businesses, which allows them to cover large claims without putting any one person or entity at significant risk.\n\n**Important Considerations:**\n\n* **Coverage Limits:** Insurance policies have coverage limits, which is the maximum amount the insurer will pay for a claim.\n* **Exclusions:**  Policies typically exclude certain events or situations from coverage.\n* **Choosing the Right Coverage:**  It's crucial to choose insurance policies that meet your specific needs and financial circumstances.\n\nIn short, insurance is a vital tool for individuals and businesses to manage risk and protect their finances against unforeseen events. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Is it good for gen z?\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Whether insurance is \"good\" for Gen Z is a complex question with no simple answer. It depends on individual circumstances, priorities, and financial situations. \n\nHere's a breakdown of the potential benefits and drawbacks:\n\n**Benefits of Insurance for Gen Z:**\n\n* **Financial Security:**  Gen Z is entering adulthood in a time of economic uncertainty and rising costs. Insurance can provide a safety net against unexpected events like job loss, medical emergencies, or property damage, mitigating financial stress.\n* **Peace of Mind:**  Knowing they have insurance can reduce anxiety about potential risks and allow them to focus on their goals and aspirations.\n* **Building Good Habits:**  Early adoption of insurance can instill good financial habits, such as planning for the future, saving money, and managing risk.\n* **Protection for the Future:**  Gen Z will likely have a long life ahead, so investing in insurance now can provide them with long-term financial security.\n* **Access to Affordable Coverage:**  Many insurance providers offer competitive rates and flexible policies specifically designed for young adults.\n\n**Drawbacks of Insurance for Gen Z:**\n\n* **Cost:**  Insurance premiums can be a significant financial burden, especially for those just starting out in their careers.\n* **Limited Need:**  Gen Z may not see the immediate need for certain types of insurance, such as life insurance or home insurance, especially if they're not homeowners or have dependents.\n* **Complexity:**  Understanding the different types of insurance and choosing the right coverage can be overwhelming.\n* **Potential for Overspending:**  Gen Z may be tempted to purchase unnecessary insurance or policies with excessive coverage, leading to wasted money.\n* **Changing Needs:**  As Gen Z progresses through life, their insurance needs may change, requiring adjustments to their policies.\n\n**The Bottom Line:**\n\n* **Assess your individual needs:**  Determine what risks are most relevant to you and prioritize insurance that aligns with your priorities and budget.\n* **Shop around:**  Compare prices and coverage options from different insurers to find the best value.\n* **Educate yourself:**  Take the time to understand the different types of insurance and how they work.\n* **Start small:**  Begin with essential insurance like health insurance and gradually expand your coverage as your needs and finances evolve.\n\nUltimately, the decision to purchase insurance is a personal one. Gen Z should carefully consider their individual circumstances and make informed choices about their insurance needs. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Is it safe to buy?\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Whether buying insurance is \"safe\" depends entirely on what you mean by safe. There are different perspectives to consider:\n\n**\"Safe\" in terms of financial security:**\n\n* **Yes:**  Insurance is designed to protect you financially from unexpected events. It provides a safety net, making it less likely you'll face significant financial hardship due to accidents, illness, or property damage.\n* **But:**  It's important to choose reputable insurance providers with strong financial stability to ensure they can fulfill their obligations in the event of a claim.\n\n**\"Safe\" in terms of avoiding scams or misleading practices:**\n\n* **Yes:** Reputable insurance companies are regulated and subject to oversight by government agencies. However, it's crucial to be aware of potential scams and to research any provider thoroughly before purchasing a policy.\n* **But:**  Be wary of unsolicited offers or high-pressure sales tactics, and always read the policy carefully before signing.\n\n**\"Safe\" in terms of getting the best value:**\n\n* **Yes:** You can make informed decisions by comparing quotes from multiple insurers, understanding coverage details, and negotiating rates.\n* **But:** Don't solely focus on price; prioritize quality coverage and reliable customer service.  \n\n**Here's how to ensure you're making a safe and smart purchase:**\n\n1. **Identify your needs:**  Determine what risks you need protection against, based on your individual situation, age, assets, and lifestyle.\n2. **Research reputable insurers:** Look for companies with solid financial ratings and positive customer reviews.\n3. **Compare quotes:**  Get quotes from multiple insurers to find the best price for comparable coverage.\n4. **Read the policy carefully:**  Understand the terms and conditions, including exclusions, limitations, and renewal procedures.\n5. **Ask questions:**  Don't hesitate to ask the insurer about anything you don't understand before committing to a policy.\n\n**Remember, insurance is a crucial part of financial planning. By taking precautions and making informed choices, you can ensure you're buying insurance that is both safe and beneficial for your future.** \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Where I can buy it?\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "You can buy insurance from various sources, both online and offline:\n\n**1. Insurance Companies Directly:**\n\n* **Their Websites:** Many insurance companies have user-friendly websites where you can get quotes, compare plans, and purchase policies online.\n* **Call Centers:** You can call their customer service lines for personalized assistance and policy inquiries.\n* **Physical Offices:** Some insurers have offices where you can meet with agents for consultations and purchase policies in person.\n\n**2. Insurance Brokers:**\n\n* **Independent Brokers:** These brokers work with multiple insurance companies and can compare different options to find you the best fit. They often provide personalized advice and guidance.\n* **Captive Brokers:** These brokers work exclusively with a specific insurance company but offer access to the company's diverse range of products.\n\n**3. Online Marketplaces:**\n\n* **Insurance Comparison Websites:** Websites like PolicyGenius, Insurify, and NerdWallet allow you to compare quotes from multiple insurers simultaneously, making it easier to find the best deal.\n\n**4. Financial Advisors:**\n\n* **Independent Financial Advisors:**  These advisors can help you develop a comprehensive financial plan that includes insurance recommendations based on your individual needs.\n* **Bank or Credit Union Advisors:**  Some banks and credit unions offer financial advice and insurance products as part of their services.\n\n**5. Employer-Sponsored Plans:**\n\n* **Group Health Insurance:** Some employers offer group health insurance plans to their employees, often with lower premiums than individual plans.\n* **Group Life Insurance:** Employers may also offer group life insurance plans to provide financial security for employees' families.\n\n**Factors to Consider When Choosing a Source:**\n\n* **Your Needs:**  Consider the type of insurance you need, your coverage requirements, and your budget.\n* **Reputable Providers:**  Choose companies with strong financial ratings and good customer service reputations.\n* **Convenience:**  Select a source that offers the buying experience and communication style that suits you best.\n* **Personalized Advice:**  If you need help understanding your options or navigating the process, consider working with a broker or advisor.\n\nRemember, regardless of the source, always carefully review the policy details before purchasing any insurance.  \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Does Gen Z need to have wider coverage in certain area?\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "You're right to ask that question! Gen Z faces unique challenges and risks that might require a slightly different approach to insurance compared to previous generations. Here are some areas where wider coverage might be particularly relevant for them:\n\n**1. Mental Health Coverage:**\n\n* Gen Z experiences higher rates of anxiety and depression than previous generations.\n* Traditional health insurance often has limited coverage for mental health services.\n* **Wider coverage:** Seeking plans with robust mental health benefits, including therapy, medication, and telehealth options, is crucial. \n\n**2. Cyber Security and Privacy:**\n\n* Gen Z grew up with technology and is heavily reliant on digital platforms.\n* This makes them vulnerable to cyberattacks, data breaches, and identity theft.\n* **Wider coverage:** Consider cyber liability insurance to protect against financial losses and legal consequences from cyberattacks, as well as identity theft protection services.\n\n**3. Student Loan Debt Protection:**\n\n* Gen Z carries a significant burden of student loan debt.\n* **Wider coverage:** Explore insurance policies that provide coverage for disability or death, which could help pay off loans in such unfortunate situations.\n\n**4. Gig Economy and Freelance Work:**\n\n* Many Gen Z members are freelancers or gig workers, lacking traditional employer-sponsored benefits.\n* **Wider coverage:**  Seek individual health insurance, disability insurance, and liability insurance to cover the risks associated with independent work.\n\n**5. Environmental Risks:**\n\n* Gen Z is facing the consequences of climate change, which can impact their property and health.\n* **Wider coverage:** Explore insurance policies that offer coverage for extreme weather events, flooding, and other climate-related risks.\n\n**6. Digital Assets and Cryptocurrency:**\n\n* Gen Z invests in digital assets, such as cryptocurrency, which carries unique risks.\n* **Wider coverage:** Look for insurance policies that protect against theft, fraud, and market fluctuations for digital assets.\n\n**7. Social Media Liability:**\n\n* Gen Z is highly active on social media, with potential risks of online defamation and copyright infringement.\n* **Wider coverage:** Consider policies that offer legal defense and financial protection against online liability claims.\n\n**It's essential for Gen Z to prioritize insurance that addresses their specific needs and protects them against modern-day risks. By carefully considering these areas and seeking out appropriate coverage, they can build a strong foundation for their financial well-being.** \n",
      ],
    },
  ]
)

response = chat_session.send_message("User input?")

print(response.text)
