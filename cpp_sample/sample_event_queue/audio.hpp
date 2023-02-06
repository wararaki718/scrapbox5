#ifndef AUDIO_HPP
#define AUDIO_HPP

#include <iostream>

#include "message.hpp"
#include "resource_id.hpp"
#include "sound_id.hpp"


class Audio
{
    public:
    static void init()
    {
        head_ = 0;
        tail_ = 0;
    }

    static void playSound(SoundId id, int volume)
    {
        for(int i = head_; i != tail_; i = (i+1)%MAX_PENDING)
        {
            if(pending_[i].id != id)
            {
                continue;
            }

            pending_[i].volume = std::max(volume, pending_[i].volume);
            return;
        }

        pending_[tail_].id = id;
        pending_[tail_].volume = volume;
        tail_++;
        tail_ %= MAX_PENDING;
    }

    static void update()
    {
        if (head_ == tail_)
        {
            return;
        }

        auto resource = loadSound(pending_[head_].id);
        int channel = findOpenChannel();
        if(channel == -1)
        {
            return;
        }

        startSound(resource, channel, pending_[head_].volume);

        head_++;
        head_ %= MAX_PENDING;
    }

    private:
    static const int MAX_PENDING = 16;
    static PlayMessage pending_[MAX_PENDING];
    static int head_;
    static int tail_;
    
    static ResourceId loadSound(SoundId id)
    {
        switch (id) {
            case SOUND_BLOOP:
                return SOUND_BLOOP_RESOURCE;
            default:
                break;
        }
        return NONE_RESOURCE;
    }

    static int findOpenChannel()
    {
        std::cout << "find open channel" << std::endl;
        return 1;
    }

    static void startSound(ResourceId id, int channel, int volume)
    {
        std::cout << "channel: " << channel << std::endl;
        std::cout << "volume: " << volume << std::endl;
        std::cout << "start sound" << std::endl;
    }
};

int Audio::head_ = 0;
int Audio::tail_ = 0;
PlayMessage Audio::pending_[] = {};

#endif // AUDIO_HPP
